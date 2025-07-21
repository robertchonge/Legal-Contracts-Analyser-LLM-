from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedContract
from .serializers import UploadedContractSerializer
from .prompts import EXTRACTION_PROMPT, SUMMARY_PROMPT
from .llm_utils import query_llm
import pdfplumber

class ContractUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = UploadedContractSerializer(data=request.data)
        if serializer.is_valid():
            contract = serializer.save()
            return Response({"contract_id": contract.id, "message": "Upload successful."})
        return Response(serializer.errors, status=400)

class AnalyzeContractView(APIView):

    def get(self, request, pk):
        try:
            contract = UploadedContract.objects.get(pk=pk)
        except UploadedContract.DoesNotExist:
            return Response({"error": "Contract not found."}, status=404)

        # Extract text from PDF
        file_path = contract.file.path
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"

        # LLM Analysis
        extraction_result = query_llm(EXTRACTION_PROMPT, text)
        summary_result = query_llm(SUMMARY_PROMPT, text)

        return Response({
            "clauses": extraction_result,
            "summary": summary_result
        })

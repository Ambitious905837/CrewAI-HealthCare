from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import markdown

from crewai import Crew
from .tasks import Tasks
from .agents import Agents

class HealthcareAIView(APIView):
    def post(self, request):
        analyze_task_desc = request.data.get('analyze_task')
        summary_task_desc = request.data.get('summary_task')
        print(analyze_task_desc)
        print(summary_task_desc)
        tasks = Tasks()
        agents = Agents()

        researcher_agent = agents.researcher_agent()
        writer_agent = agents.writer_agent()

        analyze_healthcare_ai_news = tasks.analyze_healthcare_ai_news(researcher_agent, analyze_task_desc)
        write_summaries = tasks.write_summaries(writer_agent, summary_task_desc)

        crew = Crew(
            agents=[researcher_agent, writer_agent],
            tasks=[analyze_healthcare_ai_news, write_summaries]
        )

        result = crew.kickoff()
        print(result, "-------------------")
        
        # Convert the markdown result to HTML
        html_result = markdown.markdown(result)
        
        return Response({"result": html_result}, status=status.HTTP_200_OK)

def index(request):
    return render(request, 'myapp/index.html')

from crewai import Task

class Tasks():
    def analyze_healthcare_ai_news(self, researcher_agent, description):
        return Task(
            description=description,
            expected_output="Full analysis report in bullet points",
            agent=researcher_agent
        )

    def write_summaries(self, writer_agent, description):
        return Task(
            description=description,
            expected_output="Full blog post",
            agent=writer_agent
        )

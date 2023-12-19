import anvil.server
import openai
import traceback

anvil.server.connect("your-anvil-uptime-secret")

class OrakuSantosAssistant:
    # ... existing initialization ...

    def get_api_response(self, query):
        # Modify the system message to encourage critical thinking
        system_message = """
        You are Oraku the Assistant, designed to promote critical thinking in students. 
        Instead of giving direct answers, guide the students by asking probing questions, 
        presenting multiple viewpoints, or encouraging them to explore and discover answers on their own.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": system_message},
                          {"role": "user", "content": query}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return "Error: " + str(e)

# Define a function that can be called from the Anvil app
@anvil.server.callable
def get_response_from_oraku(query):
    assistant = OrakuSantosAssistant()
    return assistant.get_api_response(query)

# Keep the server running
anvil.server.wait_forever()

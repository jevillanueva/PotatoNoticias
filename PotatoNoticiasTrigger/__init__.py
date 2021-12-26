import json
import azure.functions as func
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_webservice_support.webservice_handler import WebserviceSkillHandler
from PotatoNoticiasTrigger.default_intents import AllExceptionHandler, CancelAndStopIntentHandler, HelpIntentHandler, LaunchRequestHandler, SessionEndedRequestHandler
from PotatoNoticiasTrigger.noticias_intent import NoticiasIntentHandler
from PotatoNoticiasTrigger.config import ALEXA_SKILL_ID

def main(req: func.HttpRequest) -> func.HttpResponse:
    skill_builder = SkillBuilder()
    skill_builder.skill_id = ALEXA_SKILL_ID
    # Default Intents
    skill_builder.add_request_handler(LaunchRequestHandler())
    skill_builder.add_request_handler(HelpIntentHandler())
    skill_builder.add_request_handler(CancelAndStopIntentHandler())
    skill_builder.add_request_handler(SessionEndedRequestHandler())
    skill_builder.add_exception_handler(AllExceptionHandler())
    # Custom Intents
    skill_builder.add_request_handler(NoticiasIntentHandler())

    webservice_handler = WebserviceSkillHandler(skill=skill_builder.create())
    response = webservice_handler.verify_request_and_dispatch(req.headers, req.get_body().decode("utf-8"))
    return func.HttpResponse(json.dumps(response),mimetype="application/json")
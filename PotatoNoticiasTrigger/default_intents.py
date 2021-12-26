from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard


class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        print("Ejecucion de la Skill.")
        speech_text = "Bienvenido a Potato Noticias, puedes decir últimas noticias"
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Potato Noticias", speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print("Ejecucion Intent Ayuda")
        speech_text = "Puedes decir últimas noticias, últimos 2 mensajes"
        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("Potato Noticias - Ayuda", speech_text))
        return handler_input.response_builder.response


class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print("Ejecucion Intent Cancel o Stop")
        speech_text = "Hasta luego Atentamente Potato Noticias!"
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Eco", speech_text)).set_should_end_session(True)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # any cleanup logic goes here
        return handler_input.response_builder.response


class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        print(exception)
        speech = "Lo siento, No pude procesarlo. Puedes intentarlo nuevamente o decir Ayuda"
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name, get_slot_value
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard
from PotatoNoticiasTrigger.discord import get_n_messages
from typing import List, Tuple


def generate_response(messages):
    # type: (List) -> Tuple[str,str]
    speak_out = ""
    speak_out_visible = ""
    itemCount = 1
    for message in messages:
        speak_out += 'Mensaje {0}: <break time="0.5s"/> {1}. <break time="1s"/>'.format(
            itemCount, message.get("content", ""))
        speak_out_visible += '{0}: {1}.\n'.format(
            itemCount, message.get("content", ""))
        itemCount += 1
    return speak_out, speak_out_visible


class NoticiasIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("NoticiasIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        cantidad = get_slot_value(handler_input, "cantidad")
        print(cantidad)
        if cantidad is not None:
            messages = get_n_messages(size=cantidad)
        else:
            messages = get_n_messages()
        if messages is None or len(messages) == 0:
            speak_output = "No se encontraron mensajes"
            visual_output = "No se encontraron mensajes :("
        else:
            speak_output,visual_output = generate_response(messages)
            speak_output += " Esos son todos los mensajes!."
            visual_output += " Esos son todos los mensajes!."
        handler_input.response_builder.speak(speak_output).set_card(
            SimpleCard("Potato Noticias", visual_output)).set_should_end_session(True)
        return handler_input.response_builder.response

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionValidarSabor(Action):
    """Valida se o sabor é feito pela pizzaria"""

    def name (self) -> Text:
        return "action_validar_sabor"
    
    def run (self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sabor = tracker.get_slot("sabor")

        sabores_disponiveis = ["portuguesa", "calabresa", "frango com catupiry", "mussarela", "margherita", "picanha"]

        if sabor and sabor.lower() in [s.lower() for s in sabores_disponiveis]:
            dispatcher.utter_message(text=f"Boa escolha! Pizza de {sabor} é nossa especialidade")
            return[]
        else:
            dispatcher.utter_message(text=f"Não temos pizza de {sabor}, escolha outro sabor")
            return [SlotSet("sabor", None)]

class ActionValidarBebida(Action):
    """Valida se a bebida é feita pela pizzaria"""

    def name (self) -> Text:
        return "action_validar_bebida"
    
    def run (self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bebida = tracker.get_slot("bebida")

        bebidas_disponiveis = ["coca-cola", "guaraná", "agua", "água", "suco de laranja"]

        if bebida and bebida.lower() in [b.lower() for b in bebidas_disponiveis]:
            dispatcher.utter_message(text=f"Adicionado {bebida} ao seu pedido!")
            return[]
        else:
            dispatcher.utter_message(text=f"Não temos {bebida}, escolha outra bebida")
            return [SlotSet("bebida", None)]

class ActionSimularEntrega(Action):
    """Simula o tempo e custo de entrega com base no endereço"""

    def name (self) -> Text:
        return "action_simular_entrega"
    
    def run (self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        endereco = tracker.get_slot("endereco")
        
        # Simulação de lógica de entrega (simplificada)
        if not endereco:
             dispatcher.utter_message(text="Por favor, informe um endereço para que eu possa simular a entrega.")
             return []
             
        if "rua das flores" in endereco.lower() or "bairro novo" in endereco.lower():
            tempo = "30 minutos"
            frete = "R$ 5,00"
        elif "avenida principal" in endereco.lower() or "rua a" in endereco.lower():
            tempo = "45 minutos"
            frete = "R$ 10,00"
        else:
            tempo = "50 minutos"
            frete = "R$ 12,00"

        dispatcher.utter_message(text=f"A entrega para o endereço '{endereco}' será feita em aproximadamente {tempo}, com um custo de frete de {frete}.")
        return [SlotSet("endereco", None)] # Limpa o slot após a simulação
from ..util import create_element
from .common import EWSAccountService, create_attachment_ids_element


class DeleteAttachment(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/deleteattachment-operation
    """
    SERVICE_NAME = 'DeleteAttachment'

    def call(self, items):
        return self._chunked_get_elements(self.get_payload, items=items)

    @staticmethod
    def _get_elements_in_container(container):
        from ..properties import RootItemId
        return container.findall(RootItemId.response_tag())

    def get_payload(self, items):
        payload = create_element('m:%s' % self.SERVICE_NAME)
        attachment_ids = create_attachment_ids_element(items=items, version=self.account.version)
        payload.append(attachment_ids)
        return payload

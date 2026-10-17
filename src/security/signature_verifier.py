import hmac
import hashlib

class StripeSignatureVerifier:
    """
    Componente de Segurança Enterprise para validação do cabeçalho Stripe-Signature.
    Evita ataques de Spoofing e rejeições de contratos utilizando os bytes crus (raw body).
    """
    def __init__(self, webhook_secret: str):
        self.webhook_secret = webhook_secret.encode('utf-8')

    def verify_signature(self, payload_bytes: bytes, sig_header: str) -> bool:
        try:
            # Extrair timestamp (t) e assinaturas (v1) do cabeçalho da Stripe
            elements = dict(item.split('=', 1) for item in sig_header.split(','))
            timestamp = elements.get('t')
            signature_v1 = elements.get('v1')

            if not timestamp or not signature_v1:
                return False

            # Construção do payload assinado conforme especificação oficial da Stripe
            signed_payload = f"{timestamp}.".encode('utf-8') + payload_bytes
            
            # Cálculo do HMAC SHA256 esperado
            expected_signature = hmac.new(
                self.webhook_secret,
                signed_payload,
                hashlib.sha256
            ).hexdigest()

            # Comparação segura contra timing attacks
            return hmac.compare_digest(expected_signature, signature_v1)
        except Exception as e:
            print(f"[!] Erro na validação criptográfica de assinatura: {e}")
            return False

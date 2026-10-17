​SEC-Webhooks: Autonomous AST & Sandbox Agent
​Build Agents That Run Code: CreateOS × Stripe Projects Online Hackathon
​SEC-Webhooks é um agente autónomo de autocorreção desenhado para eliminar falhas críticas, mitigar ataques de spoofing e corrigir desvios de esquema (schema drift) em webhooks de pagamentos em tempo real, utilizando sandboxes isoladas baseadas em microVMs (CreateOS API) e análise de árvore sintática (AST).
​Arquitetura do Projeto
​O sistema está estruturado em três pilares principais localizados na diretoria sec-webhooks:
​agent/ast_engine.py: Motor de análise estática e autocorreção em tempo de execução via AST para detetar e corrigir desvios nos payloads da Stripe.
​agent/sandbox_runner.py: Gestor de comunicação via API REST com a infraestrutura CreateOS para execução segura de código em microVMs isoladas.
​tests/chaos_test.py: Laboratório de testes de caos validando resiliência contra Schema Drift, Webhook Spoofing, Retries Duplicados por TTL e Carga Massiva.
​main.py: Orquestrador principal do agente autónomo.
​Instalação e Execução (Termux / Linux)
​Certifica-te de que estás na raiz do repositório (sec-webhooks) e executa os comandos abaixo:
​Executar o Agente Autónomo (main.py)
Simula a leitura do código do webhook, análise AST e preparação para execução em sandbox:
python3 main.py
​Executar o Laboratório de Caos (chaos_test.py)
Valida os 4 cenários críticos de resiliência e mede o MTTR sob carga:
python3 tests/chaos_test.py
​Resultados dos Testes de Caos
​Schema Drift | Mutação de campos obrigatórios no payload | Passou | Correção dinâmica via AST
​Webhook Spoofing | Rejeição de assinaturas HMAC inválidas | Passou | Bloqueio imediato
​Retries Duplicados | Prevenção de reprocessamento via TTL/Cache | Passou | Deduplicação ativa
​Carga Massiva & MTTR | Estabilidade sob alta concorrência | Passou | MTTR ~35.17 ms
​Alinhamento com o Hackathon
​Agentes Autónomos: Correção de código sem intervenção humana.
​Sandboxes Seguros: Isolamento de execução via CreateOS API.
​Ecossistema Stripe: Tratamento resiliente de eventos de pagamento em produção.

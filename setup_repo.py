"""
Roda esse script UMA VEZ dentro da pasta do repositório:
  cd caminho/para/faculdade-dev-sec
  python3 setup_repo.py
"""

import os

estrutura = {
    "fase-1/modulo-1-python": [
        "aula-01-fundamentos-de-objetos",
        "aula-02-closures-e-decorators",
        "aula-03-geradores-e-iteradores",
        "aula-04-programacao-orientada-a-objetos",
        "aula-05-excecoes-e-context-managers",
        "aula-06-modulos-e-pacotes",
        "aula-07-testes-com-pytest",
        "aula-08-async-e-concorrencia",
        "aula-09-projeto-final-python",
    ],
    "fase-1/modulo-2-algoritmos": [
        "aula-01-complexidade-big-o",
        "aula-02-arrays-e-listas-ligadas",
        "aula-03-pilhas-e-filas",
        "aula-04-tabelas-hash",
        "aula-05-arvores-binarias",
        "aula-06-arvores-avl-e-bst",
        "aula-07-grafos-e-bfs-dfs",
        "aula-08-ordenacao-basica",
        "aula-09-ordenacao-avancada",
        "aula-10-programacao-dinamica",
        "aula-11-projeto-final-algoritmos",
    ],
    "fase-1/modulo-3-linux": [
        "aula-01-terminal-e-navegacao",
        "aula-02-permissoes-e-usuarios",
        "aula-03-processos-e-sinais",
        "aula-04-shell-scripting-basico",
        "aula-05-shell-scripting-avancado",
        "aula-06-systemd-e-servicos",
        "aula-07-rede-no-linux",
        "aula-08-cron-e-automacao",
        "aula-09-projeto-final-linux",
    ],
    "fase-1/modulo-4-git": [
        "aula-01-conceitos-e-primeiro-repositorio",
        "aula-02-branches-e-merge",
        "aula-03-rebase-e-cherry-pick",
        "aula-04-github-pull-requests",
        "aula-05-github-actions-intro",
        "aula-06-projeto-final-git",
    ],
    "fase-2/modulo-1-java": [
        "aula-01-sintaxe-e-tipos",
        "aula-02-oop-classes-e-objetos",
        "aula-03-heranca-e-polimorfismo",
        "aula-04-interfaces-e-abstratas",
        "aula-05-colecoes-e-generics",
        "aula-06-excecoes",
        "aula-07-io-e-arquivos",
        "aula-08-concorrencia-threads",
        "aula-09-jvm-e-memoria",
        "aula-10-projeto-final-java",
    ],
    "fase-2/modulo-2-redes": [
        "aula-01-modelo-osi-e-tcp-ip",
        "aula-02-enderecamento-ip-e-subnets",
        "aula-03-dns-dhcp-http",
        "aula-04-tls-e-criptografia-basica",
        "aula-05-wireshark-na-pratica",
        "aula-06-sockets-em-python",
        "aula-07-projeto-final-redes",
    ],
    "fase-2/modulo-3-sistemas-operacionais": [
        "aula-01-processos-e-threads",
        "aula-02-escalonamento",
        "aula-03-memoria-virtual-e-paginacao",
        "aula-04-sistema-de-arquivos",
        "aula-05-syscalls",
        "aula-06-ipc-pipes-e-sockets",
        "aula-07-projeto-final-so",
    ],
    "fase-2/modulo-4-banco-de-dados": [
        "aula-01-modelagem-relacional",
        "aula-02-sql-basico",
        "aula-03-sql-avancado-joins-subqueries",
        "aula-04-indices-e-performance",
        "aula-05-transactions-e-acid",
        "aula-06-postgresql-na-pratica",
        "aula-07-nosql-mongodb-basico",
        "aula-08-projeto-final-banco",
    ],
    "fase-3/modulo-1-backend": [
        "aula-01-apis-rest-conceitos",
        "aula-02-fastapi-primeiros-passos",
        "aula-03-autenticacao-jwt",
        "aula-04-banco-com-sqlalchemy",
        "aula-05-testes-de-integracao",
        "aula-06-documentacao-e-swagger",
        "aula-07-projeto-api-completa",
    ],
    "fase-3/modulo-2-docker": [
        "aula-01-containers-e-conceitos",
        "aula-02-dockerfile-e-imagens",
        "aula-03-volumes-e-redes",
        "aula-04-docker-compose",
        "aula-05-registry-e-boas-praticas",
        "aula-06-projeto-app-containerizado",
    ],
    "fase-3/modulo-3-cloud": [
        "aula-01-conceitos-cloud-e-aws",
        "aula-02-ec2-e-s3",
        "aula-03-iam-e-seguranca",
        "aula-04-lambda-e-serverless",
        "aula-05-vpc-e-redes-na-aws",
        "aula-06-terraform-intro",
        "aula-07-projeto-deploy-na-cloud",
    ],
    "fase-3/modulo-4-linguagem-c": [
        "aula-01-sintaxe-e-compilacao",
        "aula-02-ponteiros",
        "aula-03-alocacao-de-memoria",
        "aula-04-structs-e-unions",
        "aula-05-arquivos-e-io",
        "aula-06-buffer-overflow-introducao",
        "aula-07-projeto-final-c",
    ],
    "fase-4/modulo-1-cyber-fundamentos": [
        "aula-01-cia-triad-e-conceitos",
        "aula-02-criptografia-simetrica",
        "aula-03-criptografia-assimetrica",
        "aula-04-hashing-e-integridade",
        "aula-05-pki-e-certificados",
        "aula-06-owasp-top-10",
        "aula-07-projeto-cripto-aplicada",
    ],
    "fase-4/modulo-2-seguranca-web": [
        "aula-01-xss",
        "aula-02-sql-injection",
        "aula-03-csrf-e-ssrf",
        "aula-04-idor-e-broken-access",
        "aula-05-burp-suite-na-pratica",
        "aula-06-lab-dvwa",
        "aula-07-projeto-relatorio-web",
    ],
    "fase-4/modulo-3-pentest": [
        "aula-01-metodologia-e-fases",
        "aula-02-reconhecimento-passivo",
        "aula-03-reconhecimento-ativo-nmap",
        "aula-04-exploracao-metasploit",
        "aula-05-pos-exploracao",
        "aula-06-relatorio-tecnico",
        "aula-07-lab-hackthebox-intro",
    ],
    "fase-4/modulo-4-ctfs": [
        "aula-01-introducao-ctf-categorias",
        "aula-02-web-challenges",
        "aula-03-crypto-challenges",
        "aula-04-forensics",
        "aula-05-pwn-basico",
        "aula-06-reverse-basico",
        "writeups",
    ],
    "fase-5/modulo-1-appsec": [
        "aula-01-threat-modeling",
        "aula-02-sast-ferramentas",
        "aula-03-dast-ferramentas",
        "aula-04-revisao-de-codigo",
        "aula-05-secure-coding-python",
        "aula-06-secure-coding-java",
        "aula-07-projeto-auditoria",
    ],
    "fase-5/modulo-2-devsecops": [
        "aula-01-cicd-seguro",
        "aula-02-analise-de-dependencias",
        "aula-03-sbom",
        "aula-04-secrets-management",
        "aula-05-iac-scanning",
        "aula-06-projeto-pipeline-seguro",
    ],
    "fase-5/modulo-3-engenharia-reversa": [
        "aula-01-assembly-x86-basico",
        "aula-02-ghidra-introducao",
        "aula-03-analise-de-binario",
        "aula-04-crackmes",
        "aula-05-projeto-reversing",
    ],
    "fase-5/modulo-4-malware": [
        "aula-01-tipos-de-malware",
        "aula-02-analise-estatica",
        "aula-03-analise-dinamica-sandbox",
        "aula-04-iocs-e-deteccao",
        "aula-05-projeto-analise-de-amostra",
    ],
    "fase-6/projetos-profissionais": [
        "projeto-01-api-segura",
        "projeto-02-scanner-vulnerabilidades",
        "projeto-03-siem-simples",
        "projeto-04-relatorio-pentest-completo",
        "projeto-05-devsecops-pipeline",
    ],
    "fase-6/certificacoes": [
        "ejpt",
        "security-plus",
        "ceh",
        "oscp",
    ],
    "fase-6/ingles-tecnico": [
        "vocabulario-programacao",
        "leitura-de-docs",
        "leitura-de-cves",
        "papers",
    ],
}

readme_fase = {
    "fase-1": "# Fase 1 — Fundamentos Sólidos\n\nPython · Algoritmos · Linux · Git\n\nDuração estimada: ~6 meses\n",
    "fase-2": "# Fase 2 — Sistemas e Redes\n\nJava · Redes · Sistemas Operacionais · Banco de Dados\n\nDuração estimada: ~6 meses\n",
    "fase-3": "# Fase 3 — Backend e DevOps\n\nBackend · Docker · Cloud · C\n\nDuração estimada: ~5 meses\n",
    "fase-4": "# Fase 4 — Segurança Ofensiva\n\nCyber Security · Pentest · CTFs\n\nDuração estimada: ~6 meses\n",
    "fase-5": "# Fase 5 — AppSec e DevSecOps\n\nAppSec · DevSecOps · Engenharia Reversa · Malware\n\nDuração estimada: ~5 meses\n",
    "fase-6": "# Fase 6 — Elite\n\nProjetos Profissionais · Certificações · Inglês Técnico\n\nDuração: contínuo\n",
}

def criar_estrutura():
    criados = 0

    # README principal
    if not os.path.exists("README.md"):
        with open("README.md", "w") as f:
            f.write("# faculdade-dev-sec\n\n")
            f.write("Repositório de estudos — Engenharia de Software + Cyber Security\n\n")
            f.write("## Roadmap\n\n")
            f.write("- **Fase 1** — Fundamentos: Python, Algoritmos, Linux, Git\n")
            f.write("- **Fase 2** — Sistemas: Java, Redes, SO, Banco de Dados\n")
            f.write("- **Fase 3** — Backend e DevOps: APIs, Docker, Cloud, C\n")
            f.write("- **Fase 4** — Segurança Ofensiva: Pentest, Web Hacking, CTFs\n")
            f.write("- **Fase 5** — AppSec e DevSecOps\n")
            f.write("- **Fase 6** — Elite: Projetos, Certificações\n\n")
            f.write("Mentor: Claude (Anthropic)\n")
        print("✓ README.md criado")

    # README por fase
    for fase, conteudo in readme_fase.items():
        os.makedirs(fase, exist_ok=True)
        readme_path = os.path.join(fase, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, "w") as f:
                f.write(conteudo)
            print(f"✓ {readme_path}")

    # Pastas de aulas
    for modulo, aulas in estrutura.items():
        for aula in aulas:
            pasta = os.path.join(modulo, aula)
            os.makedirs(pasta, exist_ok=True)

            # .gitkeep para o git rastrear a pasta vazia
            gitkeep = os.path.join(pasta, ".gitkeep")
            if not os.path.exists(gitkeep):
                with open(gitkeep, "w") as f:
                    pass

            # notas.md para aulas (não para writeups/projetos)
            if aula.startswith("aula-"):
                notas = os.path.join(pasta, "notas.md")
                if not os.path.exists(notas):
                    titulo = aula.replace("-", " ").title()
                    with open(notas, "w") as f:
                        f.write(f"# {titulo}\n\n")
                        f.write("## Objetivo da aula\n\n\n")
                        f.write("## Conceitos principais\n\n\n")
                        f.write("## Vocabulário técnico (inglês)\n\n\n")
                        f.write("## Dúvidas e observações\n\n\n")

            criados += 1

    print(f"\n✅ Estrutura criada: {criados} pastas")
    print("👉 Agora vá no GitHub Desktop, faça commit de tudo e push.")

if __name__ == "__main__":
    criar_estrutura()

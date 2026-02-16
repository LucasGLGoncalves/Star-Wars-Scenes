# Star-Wars-Scenes

Aplicação web simples para **testar troca de versões de imagem** em Kubernetes.

O mesmo repositório gera 2 imagens Docker:

- `starwars-scene:v1` (tema **batalha**)
- `starwars-scene:v2` (tema **tranquilo**)

O header mostra o nome do pod para você confirmar quando o tráfego mudou.

## Build local

```bash
docker build -t <DOCKERHUB_USER>/starwars-scene:v1 \
  --build-arg SCENE=batalha \
  --build-arg HEADER_TEXT=batalha \
  ./src

docker build -t <DOCKERHUB_USER>/starwars-scene:v2 \
  --build-arg SCENE=tranquilo \
  --build-arg HEADER_TEXT=tranquilo \
  ./src


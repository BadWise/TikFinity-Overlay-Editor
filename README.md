# 🔗 Links Externos - Overlay TikFinity

## ✨ Novidade: Visualização Limpa sem Controles

Agora você pode gerar links externos que mostram **apenas os widgets**, sem nenhum menu ou controle de edição!

## 🚀 Como Usar

### 1️⃣ Configure seus Widgets
1. Abra o editor principal: `index.html`
2. Adicione e configure seus widgets TikFinity
3. Ajuste posições, tamanhos, opacidade, etc.

### 2️⃣ Gere o Link Externo
Clique no botão **🔗 Link Externo** no editor e escolha uma das 3 opções:

#### 📌 Opção 1: Via Preset (Recomendado)
```
1. Salve um preset: Botão "💾 Salvar Preset"
2. Clique em "🔗 Link Externo" > "Usar Preset"
3. Escolha o preset e copie o link

Exemplo: view.html?preset=MeuOverlay

✅ Vantagem: Se você atualizar o preset, o link reflete automaticamente!
```

#### 🔐 Opção 2: Via Configuração Codificada
```
1. Clique em "🔗 Link Externo" > "Gerar Link Agora"
2. Copie o link gerado

Exemplo: view.html?config=eyJ3aWRnZXRzIjp7IjEiOnsidXJs...

⚠️ Versão fixa - mudanças futuras não aparecem automaticamente
```

#### ⚡ Opção 3: Auto-save
```
Use simplesmente: view.html

✅ Carrega automaticamente a última configuração salva
✅ Ideal para testes rápidos
```

### 3️⃣ Use no OBS ou TikTok Studio

**No OBS:**
1. Adicione uma nova fonte > Browser
2. Cole o link completo gerado
3. Ajuste largura/altura conforme necessário
4. Marque "Shutdown source when not visible" (opcional)

**No TikTok LIVE Studio:**
1. Adicione uma nova fonte > Link Source
2. Cole o link completo gerado
3. Configure posição e tamanho

## 📊 Diferenças entre Editor e Visualização

| Recurso | index.html (Editor) | view.html (Visualização) |
|---------|-------------------|------------------------|
| Menus de controle | ✅ Sim | ❌ Não |
| Botões de edição | ✅ Sim | ❌ Não |
| Arrastar widgets | ✅ Sim | ❌ Não |
| Redimensionar | ✅ Sim | ❌ Não |
| Widgets visíveis | ✅ Sim | ✅ Sim |
| Ideal para | Configuração | Transmissão |

## 💡 Dicas

1. **Para streaming profissional**: Use a Opção 1 (Preset) - você pode atualizar o overlay sem mudar o link no OBS
2. **Para compartilhar com amigos**: Use a Opção 2 (Config codificada) - o link contém tudo
3. **Para testes rápidos**: Use a Opção 3 (Auto-save) - link simples e curto

## 🎯 Exemplos de Uso

### Exemplo 1: Preset Dinâmico
```
1. Configure widgets no editor
2. Salve como "StreamNoturna"
3. Gere link: view.html?preset=StreamNoturna
4. Use no OBS
5. Mais tarde, atualize o preset "StreamNoturna" no editor
6. O OBS mostrará as mudanças automaticamente (sem atualizar o link)
```

### Exemplo 2: Link Compartilhável
```
1. Configure widgets no editor
2. Clique "Gerar Link Agora"
3. Compartilhe o link gerado com sua equipe
4. Todos verão exatamente a mesma configuração
```

## 🛠️ Troubleshooting

**Problema: Link mostra "Nenhuma configuração encontrada"**
- Certifique-se de ter widgets configurados antes de gerar o link
- Se usar preset, verifique se salvou o preset com o nome correto
- Se usar auto-save, configure pelo menos um widget no editor

**Problema: Widgets não aparecem no OBS**
- Verifique se a URL está completa e correta
- Teste o link abrindo em uma aba normal do navegador primeiro
- Certifique-se de que o servidor está rodando

## 📝 Changelog

**v1.1** - Links Externos
- ✅ view.html criado para visualização limpa
- ✅ 3 modos de compartilhamento integrados
- ✅ Gerador de links no editor

---

**Desenvolvido para streamers do TikTok LIVE** 🎥✨

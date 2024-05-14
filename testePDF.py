from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageTemplate, Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak

def create_pdf_report(file_name, content):
    # Crie um arquivo PDF
    pdf = SimpleDocTemplate(file_name, pagesize=letter)
    
    # Estilos de parágrafo padrão
    styles = getSampleStyleSheet()
    
    # Crie um cabeçalho para o relatório
    def header(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 16)
        canvas.drawString(inch, letter[1] - inch, "Relatório de Jurimetria")
        canvas.restoreState()
    
    # Crie uma nota de rodapé com o número da página
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 9)
        canvas.drawString(inch, 0.75 * inch, f"Página {doc.page} do relatório")
        canvas.restoreState()
    
    # Crie um frame para o conteúdo do relatório
    frame = Frame(inch, inch, letter[0] - 2*inch, letter[1] - 2*inch, id='normal')
    
    # Adicione o cabeçalho e a nota de rodapé ao modelo de página
    pdf.addPageTemplates([PageTemplate(id='HeaderFooter', frames=frame, onPage=header, onPageEnd=footer)])
    
    # Crie uma lista de elementos para adicionar ao PDF
    elements = []
    
    # Adicione o conteúdo ao PDF
    for text in content:
        if text == "page_break":
            elements.append(PageBreak())
        else:
            paragraph = Paragraph(text, styles['Normal'])
            elements.append(paragraph)
    
    # Construa o PDF
    pdf.build(elements)

# Exemplo de conteúdo para o relatório
report_content = [
    "Relatório de Jurimetria",
    "Resultados:",
    "- Tempo médio de resolução por área do direito:",
    "  - Direito Civil: 730 dias",
    "  - Direito Penal: 365 dias",
    "- Principais pontos de atraso:",
    "  - Petições Iniciais: 30% do tempo total do processo",
    "  - Audiências: 20% do tempo total do processo",
    "  - Sentenças: 25% do tempo total do processo",
    "- Variação regional:",
    "  - Região Metropolitana A: Tempo Médio - 800 dias",
    "  - Região Rural B: Tempo Médio - 500 dias",
    "page_break", # Adiciona uma quebra de página
    "Nota: Os dados apresentados são fictícios e são apenas para fins ilustrativos.",
]

# Nome do arquivo PDF
pdf_file_name = "relatorio_jurimetria_com_cabecalho_e_rodape.pdf"

# Chame a função para criar o PDF
create_pdf_report(pdf_file_name, report_content)

print(f"O relatório foi salvo como '{pdf_file_name}'")

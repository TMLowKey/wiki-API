import wikipediaapi
import re


def remove_html_tags(text):
    # The regular expression pattern to match HTML tags
    tag_pattern = re.compile(r'<[^>]+>')
    # Remove the matched tags
    cleaned_text = tag_pattern.sub('', text)
    return cleaned_text

def main():
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='WikiApi (marek.tengler@protonmail.com)',
            language='cs',
            extract_format=wikipediaapi.ExtractFormat.HTML
    )

    search_term = 'Voda'

    page_html = wiki_wiki.page(search_term)

    does_page_exist = page_html.exists()


    #Check for garbage tag in wiki page, clean page_html.text so I can find first paragraph
    if '<p class="mw-empty-elt">' in page_html.text:
        first_paragraph_start = page_html.text.find('<p>', page_html.text.find('<p class="mw-empty-elt">') + 1)
    else:
        first_paragraph_start = page_html.text.find('<p>')

    first_paragraph_end = page_html.text.find('</p>', page_html.text.find('</p>') + 1) 


    search_results = wiki_wiki.search(search_term, result=10)

    print(search_results)
    print(does_page_exist)

    print(
        remove_html_tags(
            page_html.text[first_paragraph_start:first_paragraph_end]
            )
        )

if __name__ == "__main__":
    main()


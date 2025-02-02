from typing import List, Text, Tuple

import lxml

from .. import utils

MAIN_PAGE = "Anasayfa"


def extract_quotes(tree: lxml.html.HtmlElement, max_quotes: int) -> List[Text]:
    q_lst = utils.extract_quotes_li(tree, max_quotes)
    return [utils.remove_credit(q) for q in q_lst]

def qotd(html_tree: lxml.html.HtmlElement) -> Tuple[Text, Text]:
    qotd_title = html_tree.xpath('.//div[text()="Günün sözü"]')[0]
    qotd_element = qotd_title.getnext()
    qotd_components = qotd_element.xpath("center/center/table/tbody/tr")

    quote = qotd_components[0].text_content().strip()
    # how can I correctly strip newlines and quotes?
    quote = quote.replace('“', '').replace('„', '').replace('\n', '')

    author = qotd_components[1].text_content().strip()
    return quote, author

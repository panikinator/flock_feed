import spacy
from collections import Counter
from django.core.paginator import Paginator

nlp = spacy.load('en_core_web_sm')

def generate_tags(content):
    doc = nlp(content)
    
    # Extract nouns and proper nouns as potential tags
    nouns = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    
    # Get the most common nouns
    common_nouns = Counter(nouns).most_common(5)
    
    # Extract the top N tags
    tags = [tag for tag, _ in common_nouns]
    
    return tags



def is_htmx(request, boost_check=True):
    hx_boost = request.headers.get("Hx-Boosted")
    hx_request = request.headers.get("Hx-Request")
    if boost_check and hx_boost:
        return False

    elif boost_check and not hx_boost and hx_request:
        return True


def paginate(request, qs, limit=2):
    paginated_qs = Paginator(qs, limit)
    page_no = request.GET.get("page")
    return paginated_qs.get_page(page_no)

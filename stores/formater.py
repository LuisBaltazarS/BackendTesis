from collections import defaultdict
from fuzzywuzzy import fuzz

json = {
    "Carnes, Aves y Pescados": {
        "Pollo": [],
        "Res": [],
        # ... (resto de las categorías)
    },
    # ... (otras categorías)
}

def grouping_marcas(categoria, subcategoria):
    formater = {}
    plazavea = json_plazavea[categoria][subcategoria]
    tottus = json_tottus[categoria][subcategoria]

    all_marcas_plazavea = [marca['marca'] for marca in plazavea]
    all_marcas_tottus = [marca['marca'] for marca in tottus]

    all_marcas = list(set(all_marcas_plazavea + all_marcas_tottus))

    products = defaultdict(dict)

    for mc in all_marcas:
        formater[mc] = {}

    for mc in all_marcas:
        for product_plazavea in plazavea:
            for product_tottus in tottus:
                similary_products = fuzz.ratio(product_plazavea['title'], product_tottus['title'])

                if product_plazavea['marca'] == mc and product_tottus['marca'] == mc:
                    if similary_products > 15:
                        products[product_plazavea['title']] = {
                            'plazavea': [],
                            'tottus': []
                        }
                        products[product_plazavea['title']]['plazavea'].append(product_plazavea)
                        products[product_plazavea['title']]['tottus'].append(product_tottus)
                    else:
                        products[product_tottus['title']] = {
                            'plazavea': [],
                            'tottus': []
                        }
                        products[product_tottus['title']]['tottus'].append(product_tottus)
                elif product_plazavea['marca'] == mc and not product_tottus['marca']:
                    products[product_plazavea['title']] = {
                        'plazavea': [],
                        'tottus': []
                    }
                    products[product_plazavea['title']]['plazavea'].append(product_plazavea)
    return products

async def formatting():
    # Para cada sección, llama a GroupingMarcas con la categoría y subcategoría correspondientes
    # y asigna los resultados a la estructura JSON
    
    # Ejemplo para 'Carnes, Aves y Pescados'
    json['Carnes, Aves y Pescados']['Pollo'] = grouping_marcas("Carnes, Aves y Pescados", "Pollo")
    json['Carnes, Aves y Pescados']['Res'] = grouping_marcas("Carnes, Aves y Pescados", "Res")
    # ... (resto de las asignaciones)

    return json

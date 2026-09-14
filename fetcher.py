class Fetcher:
    """
        Se connecte à l'API de tracker.gg
        Récupère les données du serveur
        Construit un objet dictionnaire

    """
    def __init__(pf_riotid:str):
        riotid = pf_riotid
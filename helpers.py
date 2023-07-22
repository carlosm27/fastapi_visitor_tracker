import collections


def to_dict(psycopg_tuple:tuple):
    tracker = collections.OrderedDict()
    tracker['id'] = psycopg_tuple[0]

    tracker["ip_address"] = psycopg_tuple[1]
    tracker["request_url"] = psycopg_tuple[2]
    tracker["request_port"] = psycopg_tuple[3]
    tracker["request_path"] = psycopg_tuple[4]
    tracker["request_method"] = psycopg_tuple[5]
    tracker["browser_type"] = psycopg_tuple[6]
    tracker["request_time"] = psycopg_tuple[7].strftime("%d-%m-%Y, %H:%M:%S")
    tracker["service_name"] = psycopg_tuple[8]
    return tracker


def list_dict(rows:list):

    row_list = []
    for row in rows:
        book_dict = to_dict(row)
        row_list.append(book_dict)

    return row_list
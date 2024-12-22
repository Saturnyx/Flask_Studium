"""
def get_location(ip_address):
    try:
        response = requests.get(f"https://ipinfo.co/{ip_address}/json")
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


# Example usage
ip_address = "182.19.218.92"  # Replace with the IP address you want to look up
location_data = get_location(ip_address)
if location_data:
    print(location_data)
"""

from requests import get

loc = get("https://ipapi.co/182.19.218.92/json/")
print(loc.json())

{
    "ip": "182.19.218.92",
    "network": "182.19.208.0/20",
    "version": "IPv4",
    "city": "Singapore",
    "region": None,
    "region_code": None,
    "country": "SG",
    "country_name": "Singapore",
    "country_code": "SG",
    "country_code_iso3": "SGP",
    "country_capital": "Singapore",
    "country_tld": ".sg",
    "continent_code": "AS",
    "in_eu": False,
    "postal": "67",
    "latitude": 1.3756,
    "longitude": 103.7685,
    "timezone": "Asia/Singapore",
    "utc_offset": "+0800",
    "country_calling_code": "+65",
    "currency": "SGD",
    "currency_name": "Dollar",
    "languages": "cmn,en-SG,ms-SG,ta-SG,zh-SG",
    "country_area": 692.7,
    "country_population": 5638676,
    "asn": "AS55430",
    "org": "Starhub Ltd",
}

"""
https://github.com/geopy/geopy
"""
if __name__ == "__main__":
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="P_Stack")
    location = geolocator.geocode("175 5th Avenue NYC")   # 不适合中文
    # location = geolocator.geocode("上海市宝山区长江西路")
    print(location.address)

    print((location.latitude, location.longitude))

    # from geopy.distance import geodesic
    # newport_ri = (41.49008, -71.312796)
    # cleveland_oh = (41.499498, -81.695391)
    # print(geodesic(newport_ri, cleveland_oh).miles)
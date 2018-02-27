from time import sleep

from googleplaces import GooglePlaces, types, GooglePlacesError


MAX_FETCH = 200
google_places = GooglePlaces('AIzaSyAExIUtIyLjP5ZxnNPoYpiElnInkMrNJAI')

query_result = google_places.nearby_search(
        location='London, England', keyword='Fish and Chips',
        radius=20000, types=[types.TYPE_FOOD])
while fetched < MAX_FETCH:
  for place in query_result.places:
    print '[%i] %s' %(fetched, place.name)
    fetched = fetched + 1
  if query_result.has_next_page_token:
    sleep(3)
    print '========================================='
    print '[NPT: %s]' % query_result.next_page_token
    print '========================================='
    query_result = google_places.nearby_search(
        pagetoken=query_result.next_page_token)
import { LatLngExpression } from 'leaflet'

import { Category } from './MarkerCategories'

export interface PlaceValues {
  id: number
  position: LatLngExpression
  category: Category
  title: string
  address: string
}
export type PlacesType = PlaceValues[]
export type PlacesClusterType = Record<string, PlaceValues[]>

export const Places: PlacesType = [
  {
    id: 1,
    position: [43.4668, -80.5164],
    category: Category.CAT2,
    title: 'Some Title 1',
    address: 'Another Adress 123, Test City',
  },
]

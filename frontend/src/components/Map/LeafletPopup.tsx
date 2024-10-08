import { ChevronLeft, ChevronRight, X } from 'lucide-react'
import dynamic from 'next/dynamic'
import { Popup, PopupProps } from 'react-leaflet'
import { useRouter } from 'next/router'

import { AppConfig } from '#lib/AppConfig'
import { MarkerCategoriesValues } from '#lib/MarkerCategories'
import { PlaceValues } from '#lib/Places'
import ReviewList from '#components/Review/ReviewList'
import { useState } from 'react'

const MarkerIconWrapper = dynamic(() => import('#components/Map/LeafletMarker/MarkerIconWrapper'))
const Button = dynamic(() => import('#components/common/Button'))

interface LeafletPopupProps extends PopupProps {
  handlePopupClose: (active?: boolean) => void
  handleOpenLocation: () => void
  item: PlaceValues
  color: MarkerCategoriesValues['color']
  icon: MarkerCategoriesValues['icon']
}

const LeafletPopup = ({
  handlePopupClose,
  handleOpenLocation,
  color,
  icon,
  item,
  ...props
}: LeafletPopupProps) => {
  const { id, title, address } = item

  const router = useRouter();
  const [showReview, toggleReview] = useState(false);

  return (
    <Popup {...props}>
      <div
        className="absolute bg-white shadow"
        style={{
          // todo: rework the offsets at some point
          marginLeft: `calc(-150px + ${AppConfig.ui.markerIconSize - 5}px)`,

          // todo: some offest to align with the marker icon
          marginTop: -1,
        }}
      >
        <div className="flex flex-row justify-center pt-3" style={{ width: '300px' }}>
          <Button
            className="absolute right-3 top-3 inline-block text-dark"
            onClick={() => handlePopupClose(false)}
            small
          >
            <X size={AppConfig.ui.markerIconSize} />
          </Button>
          <div className="absolute left-0 top-0 mt-5 flex w-full justify-center">
            <MarkerIconWrapper color={color} icon={icon} />
          </div>
          <div
            className="flex w-full flex-col justify-center p-3 pt-6 text-center gap-4"
            style={{ marginTop: AppConfig.ui.markerIconSize * 2 + 8 }}
          >
            <h3 className="m-0 text-lg font-bold leading-none">{title}</h3>
            <p className="m-0 text-secondary">{address}</p>
            <Button className="gap-2 bg-slate-800 text-white rounded-lg" onClick={() => {
              toggleReview(!showReview)
              window.open('https://app.mappedin.com/map/66e5a474ecc9c8000baa8de7','_blank')
              }}>
              See Building
            </Button>
            
            {showReview && <ReviewList reviews={[              {   
                uid: "11",
                tid: "T001",
                review: "stinky ass washroom, would not go again",
                rating: 2,
              }
            ]} toilet={{
              tid: '11',
              info: 'washroom in e7',
              gender: 'Male'
            }}/>}
          </div>
        </div>
      </div>
    </Popup>
  )
}

export default LeafletPopup

import LatLngLogo from '#components/TopBar/LatLngLogo'
import { CIcon } from '@coreui/icons-react';
import { cilToilet } from '@coreui/icons';

const MapTopBar = () => (
  <div
    className="absolute left-0 top-0 flex h-20 w-full items-center bg-dark p-3 shadow"
    style={{ zIndex: 1000 }}
  >
    <div className="flex w-full text-white justify-between">
      <div className="flex flex-row items-center w-full gap-4">
        <CIcon icon={cilToilet} size="sm" className="h-14" />
        <h1 className="font-bold text-3xl">What's Your Loo?</h1>
      </div>
      <LatLngLogo />
    </div>
  </div>
)

export default MapTopBar

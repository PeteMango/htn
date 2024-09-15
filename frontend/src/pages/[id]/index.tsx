import MappedinMap from '#components/Map/mappedinE7';
import { Toilet } from '#lib/types';
import { GetServerSideProps, GetServerSidePropsContext } from 'next';

export default function Page({ data } : { data: Toilet[]}) {
    return <div className="flex flex-row">
        <div>
            <MappedinMap />
        </div>
        <div>
            reviews
        </div>
    </div>
}

export const getServerSideProps: GetServerSideProps = async (context: GetServerSidePropsContext) => {
    const id = context.query.id
    
    const response = await fetch(`http://localhost:8000/toilets_in_building?bid=${id}`);
    const data = await response.json();
    
    return { props: { data }}
}
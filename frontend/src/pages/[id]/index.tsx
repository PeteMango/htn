import { GetServerSideProps, GetServerSidePropsContext } from 'next';

export default function Page({ data }) {

}

export const getServerSideProps: GetServerSideProps = async (context: GetServerSidePropsContext) => {
    const id = context.query.id

    async function getToiletData() {
        const toilet = await fetch("http://localhost:8000/toie")
    }

    return { props: { data }}
}
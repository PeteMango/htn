import ReviewList from "#components/Review/ReviewList";
import { Review, Toilet } from "#lib/types";

export default function Test() {

    const reviews: Review[] = [
        {
            uid: "111",
            tid: "222",
            rating: 1,
            review: "was so ass, smelled so bad"
        }
    ];

    const toilet: Toilet = {
        tid: "1232132132",
        info: "washroom on floor 5 of e7",
        gender: "male"
    }

    return (
        <ReviewList reviews={reviews} toilet={toilet}/>
    )
}
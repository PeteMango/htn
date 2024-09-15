import { Review, Toilet } from "#lib/types";
import ReviewCard from "./ReviewCard";

export default function ReviewList({ reviews, toilet }: {reviews: Review[], toilet: Toilet}) {
    return (
        <div className="">
            <p className="h1">Reviews for Random Loo {toilet.tid}</p>
            {reviews.map((review) => {
                return <ReviewCard review={review}/>
            })}
        </div>
    )
}
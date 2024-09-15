import { Review, Toilet } from "#lib/types";
import ReviewCard from "./ReviewCard";

export default function ReviewList({ reviews, toilet }: {reviews: Review[], toilet: Toilet}) {
    return (
        <div className="w-full">
            <p className="text-5xl">Reviews for Random Loo {toilet.tid}</p>
            {reviews.map((review) => {
                return <ReviewCard review={review}/>
            })}
        </div>
    )
}
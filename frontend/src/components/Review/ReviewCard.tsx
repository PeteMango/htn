import { Card, CardHeader, CardTitle } from "#components/ui/card";
import { Review,  } from "#lib/types";
import { getAnonymousName } from "#lib/utils";
import { Star } from "lucide-react";

export default function ReviewCard ({ review } : { review: Review }) {
    return (
        <div className="flex flex-col p-5 rounded-lg bg-black items-center">
            <div className="flex flex-row">
                {/* {getAnonymousName(review.uid.length) Says:} */}
                {Array.from({ length: Math.floor(review.rating) }, () => (
                    <Star fill="#fbbf24" strokeWidth={0} />
                ))}
                <div className="relative w-6 h-12 overflow-hidden">
                    <Star fill="#fbbf24" strokeWidth={0} />
                </div>
            </div>
        </div>
    )
}
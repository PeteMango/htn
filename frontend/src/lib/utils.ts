import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
import { anonymousNames } from "./randomNames"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}


export function getAnonymousName(index: number) {
  return anonymousNames[index % anonymousNames.length];
}
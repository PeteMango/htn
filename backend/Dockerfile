FROM golang:1.20-alpine AS builder

WORKDIR /app

COPY go.mod ./

RUN go mod download

COPY . .

RUN go build -o main cmd/server/main.go

EXPOSE 8080

CMD ["./main"]

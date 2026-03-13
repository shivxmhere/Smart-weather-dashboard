# 🌤️ Smart Weather Dashboard

Day 1/35 of my #35DaysOfProjects challenge.

A premium web-based dashboard that fetches live weather and calculates a 
**Comfort Score** to recommend the best hours to go outside or study.

## ✨ Features
- **Modern UI**: Sleek glassmorphism design with responsive layout.
- **Intelligence**: Custom algorithm for comfort score (temp + humidity + wind).
- **Productivity**: Highlights the best window for outdoor activities or studying.
- **Serverless**: Powered by Vercel Serverless Functions.

## 🚀 Live Demo
The project is optimized for deployment on **Vercel**.

## 🛠️ How to Deploy
1. **GitHub Sync**: The project is already pushed to your repository.
2. **Import to Vercel**:
   - Go to [vercel.com](https://vercel.com) and click **"Add New"** -> **"Project"**.
   - Import `shivxmhere/Smart-weather-dashboard`.
3. **Environment Variables**:
   - In the Vercel project settings, add `OPENWEATHER_API_KEY` with your API key (`0fe762156486dbf8...`).
4. **Deploy**: Click deploy and your app will be live!

## 💻 Local Development
1. Clone the repository.
2. Install [Vercel CLI](https://vercel.com/cli): `npm i -g vercel`.
3. Run `vercel dev` to start the local server with API functions.

## Tech Stack
Python (API) · Vanilla JS · Premium CSS · Vercel

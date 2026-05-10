import { Inter } from "next/font/google";
import Script from "next/script";
import "./globals.css";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import ThemeProvider from "@/components/ThemeProvider";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "NCERT Learn — Knowledge Graph",
  description: "Navigate the NCERT Mathematics curriculum through an interconnected knowledge graph — Grades 6 to 12, 324 concepts, 497 connections",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={`${inter.className} h-full`} suppressHydrationWarning>
      <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" />
      </head>
      <body className="min-h-full flex flex-col bg-gray-50 text-gray-900 dark:bg-gray-900 dark:text-gray-100">
        <ThemeProvider>
          <Navbar />
          <main className="flex-1">{children}</main>
          <Footer />
        </ThemeProvider>
        <Script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" strategy="beforeInteractive" />
        <Script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" strategy="beforeInteractive" />
      </body>
    </html>
  );
}

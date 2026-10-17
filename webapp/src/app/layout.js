import { Inter } from "next/font/google";
import "./globals.css";
// Maths is typeset on the server now (see lib/markdown.js), so the only thing still
// needed from KaTeX is its stylesheet. Imported from the package rather than a CDN: the
// bundler emits the font files alongside it, so equations render with no network request
// and no client-side script at all.
import "katex/dist/katex.min.css";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import ThemeProvider from "@/components/ThemeProvider";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "GraphLearn — Knowledge Graph Platform",
  description: "Navigate Mathematics and Science through interconnected knowledge graphs — Grades 6 to 12, concept-by-concept learning",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={`${inter.className} h-full`} suppressHydrationWarning>
      <body className="min-h-full flex flex-col bg-gray-50 text-gray-900 dark:bg-gray-900 dark:text-gray-100">
        <ThemeProvider>
          <Navbar />
          <main className="flex-1">{children}</main>
          <Footer />
        </ThemeProvider>
      </body>
    </html>
  );
}

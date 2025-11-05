/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  async rewrites() {
    const apiBaseUrl = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:80';
    return [
      { source: "/api/:path*", destination: apiBaseUrl + "/:path*" },
    ];
  },
};
module.exports = nextConfig;

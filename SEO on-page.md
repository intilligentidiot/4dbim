| Comprehensive SEO On-Page Check List (Row Height 27) |
| ---------------------------------------------------- |
| Sr. #                                                | Particular | Description | Additional Remark |
| Technical Health                                     |
| 1                                                    | Domain Redirect Check | Every variant of the url must point to https://www. Variant | [https://example.com \| http://example.com \| http://www.example.com] -> https://www.example.com |
| 2                                                    | robots.txt | Important Allow and Disallow, And SiteMap Mention | Check Crawlabillity in Search Console |
| 3                                                    | sitemap.xml | Proper segregation of the sitemap.xml: Main, Blogs, Infographics, Projects, Misc. | Check Timestamps, Update Every 45 Days, or when content Updates. |
| 4                                                    | PageSpeed | Rough estimated current page speed checked from https://pagespeed.web.dev/ | Give any suggestion for further improvement |
| 5                                                    | Broken Pages | Check and verify broken pages from Search Console | Suggest 301 Redirect |
| 6                                                    | 404 Implementation | Proper implementation of custom 404 page. Verify header at https://httpstatus.io | Header must be 404 Code |
| 7                                                    | noindex Check | Check whether any wrong implementation of noindex tag. | <meta name="robots" content="noindex, nofollow" /> |
| 8                                                    | Identify Orphan Pages | Check and Indentify any Orphan Page exists. | No Incoming or Outgoing Links (External or Internal) |
| 9                                                    | Responsive Check | Check for Responsive Design | Use ChromeDev Tools. F12 - > Mobile Mode - Refresh and Check |
| Page Health                                          |
| Critical HTML and <head> Tags                        |
| 1                                                    | HTML Doctype Check | <!doctype> Must be defined | \- |
| 2                                                    | HTML Lang Tag | Check for <html lang="en"> | Only these values are permissible = [en, en-US, en-AU, en-IN]. Decide based on your website. |
| 3                                                    | Standard Character Set | Check whether the standard Charset is define or not. <meta charset="utf-8"> | Only UTF-8 is permissible. |
| 4                                                    | Necessary DNS-Prefetch and Preconnects | Check whether preconnectd and prefetch is there or not. | <link rel="preconnect">, <link rel="dns-prefetch"> |
| 5                                                    | Biggest Viewport Image Preload | Check for largest viewport image is preloaded or not | <link rel="preload"> |
| 4                                                    | Viewport | Check the Viewport | <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" /> |
| 7                                                    | Canonical and Hreflang | Check for <link rel="canonical"> and <link rel="alternate" hreflang=""> | Hreflang must be in set with x-default, <link rel="alternate" hreflang="x-default" href="">, <link rel="alternate" hreflang="en-us" href="">, <link rel="alternate" hreflang="en-au" href="">, <link rel="alternate" hreflang="en-ca" href="">, <link rel="alternate" hreflang="en-gb" href=""> |
| 8                                                    | Meta Keywords | Check for <meta name="keywords">, With relevant keywords. | This tag is Obslete for google but not for bing, hence, Critical. Period. |
| 9                                                    | Title and Description | Check for Title and Desctiption, Check for relevant keywrods in it. | Min 60 Chars (500 Pixels) for Title, 140 Chars (800 Pixels) for description. Max 75 Chars and 160 chars respectively. |
| 10                                                   | Robots Tag | Check for all the necessary robot tags. | <meta name="robots" content="index, follow" />, <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />, <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" /> |
| 11                                                   | OpenGraph Tags (OG Tags) | The following tags are undisputedly absolutely required. | [<meta property="og:title">, <meta property="og:locale" content="en_US">, <meta property="og:url">, <meta property="og:type">, <meta property="og:title">, <meta property="og:description">, <meta property="og:image">, <meta property="og:logo">] |
| 12                                                   | Tiwtter Card Tags | Check for twitter cards tag. | [<meta name="twitter:card" content="summary_large_image">, <meta name="twitter:site">, <meta name="twitter:title">, <meta name="twitter:description">, <meta name="twitter:image">, <meta name="twitter:image:alt">] |
| 13                                                   | Schemas | Check for proper Schema Implementation | Organisation Schema and Website Schema (Only on Homepage), Service Schema (Only on Service Pages), Breadcrumbs Schema (Every Page)-Homepage, Arcticle Schema (Blogs), Jobs Schema (Career Page) |
| 14                                                   | Google Tag Manager | Verify Google Tag Manager and Its Code. | Cross Verfiy, The Code in Tag Manager. |
| 15                                                   | Favicon | Check for <link rel="icon" type="image/x-icon" href=""> | The icon format must be ".ico" |
| 16                                                   | Apple WebView Title | Check for <meta name="apple-mobile-web-app-title" content=""> | This is crititcal for iPhone users |
| 17                                                   | Apple Touch Icons | Check for <link rel="apple-touch-icon"> | Following sizes must be defined - 57x57, 72x72, 76x76, 114x114, 120x120, 144x144, 152x152, 180x180 |
| 18                                                   | Theme Color | <meta name="theme-color"> | The hex code must be primary color of the Website. |
| 19                                                   | Head Title Check | On one <h1>, Head Titles Must be sequencial, wherever possible. | Eg. [<h1>], [<h2> <h2> ], [ <h2> <h3> <h4> ]. No LINKS in the Headings |
| 20                                                   | Image Alts and Title | Every Image must have "alt" | Very Very Important |
| 21                                                   | Image Loading | Check for image loading, "lazy" and "eager" | Please Note!! Eager for images above the first content paint and rest must be lazy. |
| 22                                                   | Explicit Image Size | Every Image must have "width" and "height" clearly mentioned | This is critical for page speed |
| 23                                                   | Image Format | Check for not-permissible image formats - png and jpg. ONLY WEBP, SVG, GIF | Use ChromeDev Tools. F12 - > Network - Refresh and Check |
| 24                                                   | Anchor Texts | Every anchor text on the Domain must have "title" Attribute | "title" must not take the value of the Anchor. Period. Title must be descriptive if necessary. |
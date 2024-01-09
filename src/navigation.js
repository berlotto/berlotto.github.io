import { getPermalink, getBlogPermalink, getAsset } from './utils/permalinks';

export const headerData = {
  links: [ 
    {
      text: 'Artigos do Blog',
      href: getBlogPermalink(),
    },
    // {
    //   text: 'Currículo Profissional',
    //   href: getPermalink('/homes/personal'),
    // },
  ],
  // actions: [{ text: 'Download', href: 'https://github.com/onwidget/astrowind', target: '_blank' }],
};

export const footerData = {
  links: [
    // {
    //   title: 'Redes',
    //   links: [
    //     { text: 'X', icon: 'tabler:brand-x', href: 'https://twitter.com/btto678' },
    //     { text: 'Instagram', icon: 'tabler:brand-instagram', href: 'https://www.instagram.com/sberlotto/' },
    //     { text: 'Linkedin', icon: 'tabler:brand-linkedin', href: 'https://www.linkedin.com/in/sergioberlotto/' },
    //     { text: 'RSS', icon: 'tabler:rss', href: getAsset('/rss.xml') },
    //     { text: 'Github', icon: 'tabler:brand-github', href: 'https://github.com/berlotto/' },
    //   ],
    // },
  ],
  // secondaryLinks: [
  //   { text: 'Terms', href: getPermalink('/terms') },
  //   { text: 'Privacy Policy', href: getPermalink('/privacy') },
  // ],
  socialLinks: [
    { ariaLabel: 'X', icon: 'tabler:brand-x', href: 'https://twitter.com/btto678' },
    { ariaLabel: 'Instagram', icon: 'tabler:brand-instagram', href: 'https://www.instagram.com/sberlotto/' },
    { ariaLabel: 'Linkedin', icon: 'tabler:brand-linkedin', href: 'https://www.linkedin.com/in/sergioberlotto/' },
    { ariaLabel: 'RSS', icon: 'tabler:rss', href: getAsset('/rss.xml') },
    { ariaLabel: 'Github', icon: 'tabler:brand-github', href: 'https://github.com/berlotto/' },
  ],
  // footNote: `
    
  // `,
};

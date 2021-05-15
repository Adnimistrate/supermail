module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ],
  configureWebpack:{
    resolve:{
      alias:{
        //省略引用的时候要写.././
        'assets':'@/assets',
        'common':'@/common',
        'components':'@/components',
        'network':'@/network',
        'views':'@/views'
      }
    }
  }
}

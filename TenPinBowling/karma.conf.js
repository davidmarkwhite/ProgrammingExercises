
module.exports = function(config) {
  config.set({

    basePath: '',

    frameworks: ['mocha','chai'],

    files: [
      'src/*.js',
      'test/*.spec.js'
    ],

    reporters: ['spec'],

    port: 9876,

    colors: true,

    logLevel: config.LOG_INFO,

    autoWatch: true,

    browsers: ['PhantomJS'],

    singleRun: true
  });
};

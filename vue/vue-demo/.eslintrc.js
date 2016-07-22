module.exports = {
  root: true,
  extends: 'airbnb/base',
  // required to lint *.vue files
  plugins: [
    'html'
  ],
  // add your custom rules here
  'rules': {
    'strice': 0,
    'quotes': 0,
    'arrow-body-style': ['error', 'always'],
    'no-shadow': ['error', { 'builtinGlobals': false, 'hoist': 'never', 'allow': ['state'] }],
    'no-param-reassign':  ['error', { 'props': false,}],
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
  }
}

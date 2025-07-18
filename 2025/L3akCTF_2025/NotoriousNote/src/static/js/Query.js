(function(global){

  global.MakeQueryArg = function(){

    const QueryArg = function(){
      return QueryArg.get.apply(global, arguments);
    };

    QueryArg.version = "1.0.0";

    QueryArg.parseQuery = function(s){
      if (!s) return {};
      if (s.indexOf("=") === -1 && s.indexOf("&") === -1) return {};
      s = QueryArg._qaCleanParamStr(s);
      const obj = {};
      const pairs = s.split("&");
      pairs.forEach(pair => {
        if (!pair) return;
        const [rawKey, ...rest] = pair.split("=");
        const key = decodeURIComponent(rawKey);
        // Join the rest in case the value contains '='
        const rawValue = rest.length > 0 ? rest.join("=") : "";
        const val = QueryArg._qaDecode(rawValue);
        QueryArg._qaAccess(obj, key, val);
      });
      return obj;
    };

    QueryArg._qaDecode = function(s) {
      if (!s) return "";
      while (s.indexOf("+") > -1) {
        s = s.replace("+", " ");
      }
      return decodeURIComponent(s);
    };

    QueryArg._qaAccess = function(obj, selector, value) {
      const shouldSet = typeof value !== "undefined";
      let selectorBreak = -1;
      const coerce_types = {
        'true'  : true,
        'false' : false,
        'null'  : null
      };

      if (typeof selector === 'string' || Object.prototype.toString.call(selector) === '[object String]') {
        selectorBreak = selector.search(/[\.\[]/);
      }

      if (selectorBreak === -1) {
        if (QueryArg.coerceMode) {
          value = value && !isNaN(value)            ? +value
                : value === 'undefined'             ? undefined
                : coerce_types[value] !== undefined ? coerce_types[value]
                : value;
        }
        return shouldSet ? (obj[selector] = value) : obj[selector];
      }

      const currentRoot = selector.substr(0, selectorBreak);
      let nextSelector = selector.substr(selectorBreak + 1);

      switch (selector.charAt(selectorBreak)) {
        case '[':
          obj[currentRoot] = obj[currentRoot] || [];
          nextSelector = nextSelector.replace(']', '');

          if (nextSelector.search(/[\.\[]/) === -1 && nextSelector.search(/^[0-9]+$/) > -1) {
            nextSelector = parseInt(nextSelector, 10);
          }

          return QueryArg._qaAccess(obj[currentRoot], nextSelector, value);
        case '.':
          obj[currentRoot] = obj[currentRoot] || {};
          return QueryArg._qaAccess(obj[currentRoot], nextSelector, value);
      }

      return obj;
    };

    QueryArg.coerceMode = true;

    QueryArg._qaCleanParamStr = function(s){
      if (s.indexOf("?") > -1)
        s = s.split("?")[1];

      if (s.indexOf("#") > -1)
        s = s.split("#")[1];

      if (s.indexOf("=") === -1 && s.indexOf("&") === -1)
        return "";

      while (s.indexOf("#") === 0 || s.indexOf("?") === 0)
        s = s.substr(1);

      return s;
    };

    return QueryArg;

  };

  if (typeof define === 'function' && define.amd) {
    define(function(){
      return MakeQueryArg();
    });
  } else if (typeof module === 'object' && module.exports) {
    module.exports = MakeQueryArg();
  } else {
    global.QueryArg = MakeQueryArg();
  }

})(window);
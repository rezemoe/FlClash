import re
import sys

def patch_file(path):
    with open(path, 'r') as f:
        content = f.read()

    target = "@JsonKey(name: 'route-address') List<String> get routeAddress;"
    replacement = "@JsonKey(name: 'route-address') List<String> get routeAddress;@JsonKey(name: 'exclude-package') List<String> get excludePackage;@JsonKey(name: 'exclude-interface') List<String> get excludeInterface;"
    content = content.replace(target, replacement)

    target = "&&const DeepCollectionEquality().equals(other.routeAddress, routeAddress));"
    replacement = "&&const DeepCollectionEquality().equals(other.routeAddress, routeAddress)&&const DeepCollectionEquality().equals(other.excludePackage, excludePackage)&&const DeepCollectionEquality().equals(other.excludeInterface, excludeInterface));"
    content = content.replace(target, replacement)

    target = "&&const DeepCollectionEquality().equals(other._routeAddress, _routeAddress));"
    replacement = "&&const DeepCollectionEquality().equals(other._routeAddress, _routeAddress)&&const DeepCollectionEquality().equals(other._excludePackage, _excludePackage)&&const DeepCollectionEquality().equals(other._excludeInterface, _excludeInterface));"
    content = content.replace(target, replacement)

    target = "const DeepCollectionEquality().hash(routeAddress));"
    replacement = "const DeepCollectionEquality().hash(routeAddress),const DeepCollectionEquality().hash(excludePackage),const DeepCollectionEquality().hash(excludeInterface));"
    content = content.replace(target, replacement)
    
    target = "const DeepCollectionEquality().hash(_routeAddress));"
    replacement = "const DeepCollectionEquality().hash(_routeAddress),const DeepCollectionEquality().hash(_excludePackage),const DeepCollectionEquality().hash(_excludeInterface));"
    content = content.replace(target, replacement)

    target = "routeAddress: $routeAddress)';\n"
    replacement = "routeAddress: $routeAddress, excludePackage: $excludePackage, excludeInterface: $excludeInterface)';\n"
    content = content.replace(target, replacement)
    target = "@JsonKey(name: 'route-address') List<String> routeAddress"
    replacement = "@JsonKey(name: 'route-address') List<String> routeAddress,@JsonKey(name: 'exclude-package') List<String> excludePackage,@JsonKey(name: 'exclude-interface') List<String> excludeInterface"
    content = content.replace(target, replacement)

    target = "_that.routeAddress);"
    replacement = "_that.routeAddress,_that.excludePackage,_that.excludeInterface);"
    content = content.replace(target, replacement)

    target = "Object? routeAddress = null,"
    replacement = "Object? routeAddress = null,Object? excludePackage = null,Object? excludeInterface = null,"
    content = content.replace(target, replacement)

    target = "routeAddress: null == routeAddress ? _self.routeAddress : routeAddress // ignore: cast_nullable_to_non_nullable\nas List<String>,"
    replacement = "routeAddress: null == routeAddress ? _self.routeAddress : routeAddress // ignore: cast_nullable_to_non_nullable\nas List<String>,\nexcludePackage: null == excludePackage ? _self.excludePackage : excludePackage // ignore: cast_nullable_to_non_nullable\nas List<String>,\nexcludeInterface: null == excludeInterface ? _self.excludeInterface : excludeInterface // ignore: cast_nullable_to_non_nullable\nas List<String>,"
    content = content.replace(target, replacement)

    target = "@JsonKey(name: 'route-address') final  List<String> routeAddress = const []}): _dnsHijack = dnsHijack,_routeAddress = routeAddress;"
    replacement = "@JsonKey(name: 'route-address') final  List<String> routeAddress = const [], @JsonKey(name: 'exclude-package') final  List<String> excludePackage = const [], @JsonKey(name: 'exclude-interface') final  List<String> excludeInterface = const []}): _dnsHijack = dnsHijack,_routeAddress = routeAddress,_excludePackage = excludePackage,_excludeInterface = excludeInterface;"
    content = content.replace(target, replacement)

    target = "@override@JsonKey(name: 'auto-route') final  bool autoRoute;"
    replacement = "@override@JsonKey(name: 'auto-route') final  bool autoRoute;\n  final  List<String> _excludePackage;\n  @override\n  @JsonKey(name: 'exclude-package')\n  List<String> get excludePackage {\n    if (_excludePackage is EqualUnmodifiableListView) return _excludePackage;\n    // ignore: implicit_dynamic_type\n    return EqualUnmodifiableListView(_excludePackage);\n  }\n\n  final  List<String> _excludeInterface;\n  @override\n  @JsonKey(name: 'exclude-interface')\n  List<String> get excludeInterface {\n    if (_excludeInterface is EqualUnmodifiableListView) return _excludeInterface;\n    // ignore: implicit_dynamic_type\n    return EqualUnmodifiableListView(_excludeInterface);\n  }"
    content = content.replace(target, replacement)

    with open(path, 'w') as f:
        f.write(content)
        
patch_file('lib/models/generated/clash_config.freezed.dart')

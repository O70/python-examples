# GitLab Data Migration

Access Token: `TEoi3qgzkem7E4Gx4JE1`

Public Project:
``` sh
$ curl -o tmp/projects.json http://gitlab.riped.com/api/v4/projects
```

``` sh
$ curl -o tmp/projects.json --header "PRIVATE-TOKEN: TEoi3qgzkem7E4Gx4JE1" "http://gitlab.riped.com/api/v4/projects"
```

All Groups:
``` sh
$ curl -o tmp/groups.json --header "PRIVATE-TOKEN: TEoi3qgzkem7E4Gx4JE1" "http://gitlab.riped.com/api/v4/groups"
```



vim:
  pkg.installed:
    - name: {{ salt['pillar.get']('example.package') }}

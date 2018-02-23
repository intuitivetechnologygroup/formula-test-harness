install-vim:
  pkg.installed:
    - name: {{ pillar['example']['package'] }}

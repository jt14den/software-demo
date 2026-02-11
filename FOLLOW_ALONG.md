# Follow-Along Guide: Making Research Software Citable & Discoverable
**UC Love Data Week 2026**

---

## Quick Start (5 minutes)

### 1. Clone the Demo Repository

```bash
git clone https://github.com/jt14den/software-demo.git
cd software-demo
```

### 2. Explore the Six States

The repository has 6 branches showing the progression from fragile code to FAIR research software:

```bash
git checkout 01-start      # Initial fragile state
git checkout 02-license    # Added LICENSE
git checkout 03-pixi       # Added environment management
git checkout 04-citation   # Added CITATION.cff
git checkout 05-release    # Tagged for release
git checkout 06-metadata   # Final FAIR state
```

---

## Following the Presentation

### **Section 1: The Problem (Slides 1-5)**

**Checkout the broken code:**
```bash
git checkout 01-start
ls -la
```

**What you'll see:**
- Minimal README
- No LICENSE
- No environment setup
- No citation information

---

### **Section 2: Example of "Done Right" (Slide 6)**

**View a production example:**
- Browse to: https://github.com/spack/spack
- Notice: LICENSE, CITATION.cff, README, docs

---

### **Section 3: Licensing (Slides 7-13)**

**Checkout the licensed version:**
```bash
git checkout 02-license
cat LICENSE
cat README.md
```

**What changed:**
- ✅ BSD 3-Clause LICENSE file added
- ✅ README updated with license section

**Key takeaway:** Without a license, your code isn't legally reusable.

---

### **Section 4: Environments with pixi (Slides 14-18)**

**Checkout the environment-managed version:**
```bash
git checkout 03-pixi
cat pixi.toml
cat .gitignore
ls -la
```

**What changed:**
- ✅ `pixi.toml` (environment definition)
- ✅ `pixi.lock` (locked dependencies)
- ✅ `.gitignore` (excludes .pixi/ folder)

**Try it (if you have pixi installed):**
```bash
pixi install
pixi run python src/analysis.py
```

**Key takeaway:** Reproducible environments ensure "works on my machine" becomes "works everywhere."

---

### **Section 5: Citation (Slides 19-20)**

**Checkout the citation-ready version:**
```bash
git checkout 04-citation
cat CITATION.cff
```

**What changed:**
- ✅ `CITATION.cff` file with author metadata

**View on GitHub:**
- Go to: https://github.com/jt14den/software-demo
- Look for the **"Cite this repository"** button (right sidebar)

**Key takeaway:** CITATION.cff makes it easy for others to cite your work correctly.

---

### **Section 6: DOI (Slides 21-23)**

**Checkout the release-ready version:**
```bash
git checkout 05-release
git tag -l
git log --oneline
```

**What changed:**
- ✅ Git tag `v0.1.0` created
- ✅ Ready for GitHub Release → Zenodo DOI

**GitHub Release workflow:**
1. Create tag: `git tag v0.1.0`
2. Push tag: `git push --tags`
3. Create GitHub Release (via web UI)
4. Zenodo automatically archives and mints DOI

**Key takeaway:** DOIs provide permanent, citable identifiers that never break.

---

### **Section 7: README (Slides 24-28)**

**Checkout the fully documented version:**
```bash
git checkout 06-metadata
cat README.md
cat .zenodo.json
ls -la
```

**What changed:**
- ✅ Professional README with installation, usage, citation
- ✅ `.zenodo.json` (rich metadata for archiving)
- ✅ `CONTRIBUTING.md` (community guidelines)
- ✅ `CODE_OF_CONDUCT.md` (behavioral standards)

**Key takeaway:** A good README is your software's front door.

---

## Final State Checklist

**In branch `06-metadata`, you now have:**

✅ **F - Findable**
- DOI badge in README
- CITATION.cff file
- Rich metadata (.zenodo.json)

✅ **A - Accessible**
- Public GitHub repository
- Archived on Zenodo
- Standard git clone workflow

✅ **I - Interoperable**
- Standard file formats (YAML, CFF)
- Documented dependencies (pixi.toml)
- Clear environment setup

✅ **R - Reusable**
- BSD 3-Clause LICENSE
- Professional README
- Environment reproducibility
- Community standards (CONTRIBUTING, CODE_OF_CONDUCT)

---

## Quick Command Reference

### View Different States:
```bash
git checkout 01-start      # Fragile code
git checkout 02-license    # + LICENSE
git checkout 03-pixi       # + Environment
git checkout 04-citation   # + CITATION.cff
git checkout 05-release    # + Release tag
git checkout 06-metadata   # + Full documentation
```

### Explore Files:
```bash
cat README.md              # View README
cat LICENSE                # View license
cat CITATION.cff           # View citation info
cat pixi.toml              # View environment
tree -L 2 -I .git          # View directory structure
```

### View Commits:
```bash
git log --oneline --all    # See all commits
git log --graph --all      # Visual commit history
git diff 01-start 06-metadata  # Compare start vs end
```

---

## Try It Yourself

### Option 1: Fork and Modify
1. Fork https://github.com/jt14den/software-demo
2. Clone your fork
3. Make changes (update README, add your name to CITATION.cff)
4. Commit and push

### Option 2: Create Your Own
1. Create a new repository on GitHub
2. Follow the pattern from software-demo
3. Add: LICENSE → pixi.toml → CITATION.cff → README
4. Create a release and link to Zenodo Sandbox

---

## Resources

**Demo Repository:**
https://github.com/jt14den/software-demo

**Lesson Materials:**
https://jt14den.github.io/research-software-citable-discoverable/

**Tools:**
- Choose a License: https://choosealicense.com
- CITATION.cff Helper: https://citation-file-format.github.io/cff-initializer-javascript/
- Pixi: https://pixi.sh
- Zenodo Sandbox: https://sandbox.zenodo.org
- UC OSPO: https://ucospo.net

**UC-Specific Resources:**
- UC OSS Chart: https://security.ucop.edu/files/documents/resources/oss-chart.pdf
- UC OSPO License Guide: https://ucospo.net/oss-resources/template-guides/license-guide/
- UC OSPO README Guide: https://ucospo.net/oss-resources/template-guides/readme-guide/

---

## Questions?

**Presenters:**
- Tim Dennis (UCLA): tdennis@library.ucla.edu
- Leigh Phan (UCLA): leighphan@library.ucla.edu
- Reid Otsuji (UCSD): rotsuji@ucsd.edu
- Karla Padilla (UCSD): kpadilla@ucsd.edu

**Report issues or suggest improvements:**
https://github.com/carpentries-incubator/research-software-citable-discoverable/issues

---

**🚀 You now have a roadmap for making your research software FAIR!**

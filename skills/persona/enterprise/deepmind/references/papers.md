# DeepMind Key Papers

## Foundational Papers

### Deep Q-Networks (DQN)

**Title:** Human-level control through deep reinforcement learning

**Authors:** Mnih et al.

**Venue:** Nature, 2015

**Contribution:** First deep RL system to play Atari games at human level from raw pixels

**Key Innovation:** Experience replay + target networks for stable Q-learning

```bibtex
@article{mnih2015human,
  title={Human-level control through deep reinforcement learning},
  author={Mnih, Volodymyr and Kavukcuoglu, Koray and Silver, David and Rusu, Andrei A and Veness, Joel and Bellemare, Marc G and Graves, Alex and Riedmiller, Martin and Fidjeland, Andreas K and Ostrovski, Georg and others},
  journal={Nature},
  volume={518},
  pages={529--533},
  year={2015}
}
```

---

## Alpha Series

### AlphaGo

**Title:** Mastering the game of Go with deep neural networks and tree search

**Authors:** Silver et al.

**Venue:** Nature, 2016

**Contribution:** First computer program to defeat professional Go player

```bibtex
@article{silver2016mastering,
  title={Mastering the game of Go with deep neural networks and tree search},
  author={Silver, David and Huang, Aja and Maddison, Chris J and Guez, Arthur and Sifre, Laurent and Van Den Driessche, George and Schrittwieser, Julian and Antonoglou, Ioannis and Panneershelvam, Veda and Lanctot, Marc and others},
  journal={Nature},
  volume={529},
  pages={484--489},
  year={2016}
}
```

### AlphaGo Zero

**Title:** Mastering the game of Go without human knowledge

**Authors:** Silver et al.

**Venue:** Nature, 2017

**Contribution:** Superhuman Go from self-play only, no human data

```bibtex
@article{silver2017mastering,
  title={Mastering the game of Go without human knowledge},
  author={Silver, David and Schrittwieser, Julian and Simonyan, Karen and Antonoglou, Ioannis and Huang, Aja and Guez, Arthur and Hubert, Thomas and Baker, Lucas and Lai, Matthew and Bolton, Adrian and others},
  journal={Nature},
  volume={550},
  pages={354--359},
  year={2017}
}
```

### AlphaZero

**Title:** A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play

**Authors:** Silver et al.

**Venue:** Science, 2018

**Contribution:** Same algorithm masters three games without game-specific tuning

```bibtex
@article{silver2018general,
  title={A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play},
  author={Silver, David and Hubert, Thomas and Schrittwieser, Julian and Antonoglou, Ioannis and Lai, Matthew and Guez, Arthur and Lanctot, Marc and Sifre, Laurent and Kumaran, Dharshan and Graepel, Thore and others},
  journal={Science},
  volume={362},
  pages={1140--1144},
  year={2018}
}
```

### MuZero

**Title:** Mastering Atari, Go, chess and shogi by planning with a learned model

**Authors:** Schrittwieser et al.

**Venue:** Nature, 2020

**Contribution:** Model-based planning without knowing environment dynamics

```bibtex
@article{schrittwieser2020mastering,
  title={Mastering Atari, Go, chess and shogi by planning with a learned model},
  author={Schrittwieser, Julian and Antonoglou, Ioannis and Hubert, Thomas and Simonyan, Karen and Sifre, Laurent and Schmitt, Simon and Guez, Arthur and Lockhart, Edward and Hassabis, Demis and Graepel, Thore and others},
  journal={Nature},
  volume={588},
  pages={604--609},
  year={2020}
}
```

---

## AlphaFold Series

### AlphaFold

**Title:** Improved protein structure prediction using potentials from deep learning

**Authors:** Senior et al.

**Venue:** Nature, 2020

**Contribution:** First competitive protein structure prediction using deep learning

```bibtex
@article{senior2020improved,
  title={Improved protein structure prediction using potentials from deep learning},
  author={Senior, Andrew W and Evans, Richard and Jumper, John and Kirkpatrick, James and Sifre, Laurent and Green, Tim and Qin, Chongli and Zidek, Augustin and Nelson, Alexander WR and Bridgland, Alex and others},
  journal={Nature},
  volume={577},
  pages={706--710},
  year={2020}
}
```

### AlphaFold 2

**Title:** Highly accurate protein structure prediction with AlphaFold

**Authors:** Jumper et al.

**Venue:** Nature, 2021

**Contribution:** Solved 50-year protein folding problem; **Nobel Prize 2024**

**Key Innovations:** Evoformer, Invariant Point Attention, FAPE loss

```bibtex
@article{jumper2021highly,
  title={Highly accurate protein structure prediction with AlphaFold},
  author={Jumper, John and Evans, Richard and Pritzel, Alexander and Green, Tim and Figurnov, Michael and Ronneberger, Olaf and Tunyasuvunakool, Kathryn and Bates, Russ and {\v{Z}}{\'\i}dek, Augustin and Potapenko, Anna and others},
  journal={Nature},
  volume={596},
  pages={583--589},
  year={2021}
}
```

### AlphaFold 3

**Title:** Accurate structure prediction of biomolecular interactions with AlphaFold 3

**Authors:** Abramson et al.

**Venue:** Nature, 2024

**Contribution:** Extends to DNA, RNA, ligands, ions; diffusion-based architecture

```bibtex
@article{abramson2024accurate,
  title={Accurate structure prediction of biomolecular interactions with AlphaFold 3},
  author={Abramson, Josh and Adler, Jonas and Dunger, Jack and Evans, Richard and Green, Tim and Pritzel, Alexander and Ronneberger, Olaf and Willmore, Lindsay and Ballard, Andrew J and Bambrick, Joshua and others},
  journal={Nature},
  volume={630},
  pages={493--500},
  year={2024}
}
```

---

## Mathematics

### AlphaGeometry

**Title:** Solving olympiad geometry without human demonstrations

**Authors:** Trinh et al.

**Venue:** Nature, 2024

**Contribution:** IMO-level geometry without human proofs for training

```bibtex
@article{trinh2024solving,
  title={Solving olympiad geometry without human demonstrations},
  author={Trinh, Trieu H and Wu, Yuhuai and Le, Quoc V and He, He and Luong, Thang},
  journal={Nature},
  volume={625},
  pages={476--482},
  year={2024}
}
```

### AlphaProof

**Title:** Olympiad-level formal mathematical reasoning with reinforcement learning

**Authors:** Hubert et al.

**Venue:** Nature, 2025

**Contribution:** IMO 2024 silver medal performance in formal mathematics

**Key Innovation:** Reinforcement learning in Lean proof assistant

---

## Multimodal & Language

### Gemini 1.0

**Title:** Gemini: A Family of Highly Capable Multimodal Models

**Authors:** Gemini Team

**Venue:** arXiv, 2023

**Contribution:** Native multimodal foundation model from Brain+DeepMind collaboration

```bibtex
@article{team2023gemini,
  title={Gemini: A Family of Highly Capable Multimodal Models},
  author={{Gemini Team}},
  journal={arXiv preprint arXiv:2312.11805},
  year={2023}
}
```

### Gemini 1.5

**Title:** Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens

**Authors:** Gemini Team

**Venue:** arXiv, 2024

**Contribution:** 1M+ token context, MoE architecture

---

## Other Notable Papers

### WaveNet

**Title:** WaveNet: A Generative Model for Raw Audio

**Authors:** Oord et al.

**Venue:** arXiv, 2016

**Contribution:** Revolutionary speech synthesis, used in Google Assistant

```bibtex
@article{oord2016wavenet,
  title={WaveNet: A Generative Model for Raw Audio},
  author={van den Oord, A{\"a}ron and Dieleman, Sander and Zen, Heiga and Simonyan, Karen and Vinyals, Oriol and Graves, Alex and Kalchbrenner, Nal and Senior, Andrew and Kavukcuoglu, Koray},
  journal={arXiv preprint arXiv:1609.03499},
  year={2016}
}
```

### Neural Architecture Search

**Title:** Neural Architecture Search with Reinforcement Learning

**Authors:** Zoph & Le

**Venue:** ICLR, 2017

**Contribution:** RL to design neural network architectures

### Distributed RL

**Title:** IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures

**Authors:** Espeholt et al.

**Venue:** ICML, 2018

**Contribution:** Scalable distributed RL for multi-task learning

```bibtex
@inproceedings{espeholt2018impala,
  title={IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures},
  author={Espeholt, Lasse and Soyer, Hubert and Munos, Remi and Simonyan, Karen and Mnih, Volodymyr and Ward, Tom and Doron, Yotam and Firoiu, Vlad and Harley, Tim and Dunning, Iain and others},
  booktitle={International Conference on Machine Learning},
  pages={1407--1416},
  year={2018}
}
```

---

## Reading Guide

### For RL/Games
1. DQN (2015) — Foundation
2. AlphaGo (2016) — MCTS + deep networks
3. AlphaGo Zero (2017) — Self-play
4. AlphaZero (2018) — Generalization
5. MuZero (2020) — Model-based

### For Protein Structure
1. AlphaFold (2020) — First competitive results
2. AlphaFold 2 (2021) — Breakthrough (**essential**)
3. AlphaFold 3 (2024) — General biomolecules

### For Multimodal AI
1. Gemini 1.0 (2023) — Native multimodality
2. Gemini 1.5 (2024) — Long context

### For Mathematical Reasoning
1. AlphaGeometry (2024) — Geometry
2. AlphaProof (2025) — Formal proofs

---

## Accessing Papers

| Resource | URL |
|----------|-----|
| DeepMind Publications | https://deepmind.google/research/publications/ |
| AlphaFold | https://www.nature.com/articles/s41586-021-03819-2 |
| AlphaFold 3 | https://www.nature.com/articles/s41586-024-07487-w |
| arXiv | https://arxiv.org/search/?query=deepmind |
| Google Scholar | Search "DeepMind" + topic |

---

## Citation Impact

| Paper | Citations (approx.) |
|-------|---------------------|
| DQN (2015) | 15,000+ |
| AlphaGo (2016) | 10,000+ |
| AlphaGo Zero (2017) | 8,000+ |
| AlphaZero (2018) | 5,000+ |
| AlphaFold 2 (2021) | 12,000+ |
| WaveNet (2016) | 8,000+ |

*Citation counts approximate as of 2024*

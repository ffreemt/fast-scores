"""Test process_en."""
from fast_scores.process_en import process_en

text_en0 = [
    "Copyright © Foreign Language Teaching and Research Press 2016",
    "All rights reserved. No part of this publication may be reproduced or distributed by any means, or stored in a database or retrieval system, without the prior written permission of Foreign Language Teaching and Research Press.",
    "Published by Foreign Language Teaching and Research Press",
    "No. 19 Xisanhuan Beilu",
    "http://www.fltrp.com",
    "The Tempest",
    "Copyright©The Royal Shakespeare Company, 2007",
    "All rights reserved",
    "Published by arrangement with Random House, an imprint of the Random House Publishing Group, a division of Random House, Inc.",
    "ISBN 978-7-5135-7223-1",
]


def test_process_en():
    """Test process_en."""
    assert [*map(len, process_en(text_en0))] == [8, 21, 6, 4, 1, 1, 5, 2, 9, 2]

    [*map(len, process_en(text_en0, remove_en_stopwords=False))] == [
        9,
        33,
        8,
        4,
        1,
        2,
        5,
        3,
        14,
        2,
    ]

    assert [*map(len, process_en(text_en0, dedup=False))] == [
        8,
        21,
        6,
        4,
        1,
        1,
        5,
        2,
        13,
        2,
    ]

# -*- coding: utf-8 -*-
# @Date    : 2017/10/29
# @Author  : hrwhisper
import os

from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from xgboost import XGBClassifier

from common_helper import ModelBase
from use_category2 import CategoryToVec2
from use_location import LocationToVec2
from use_price import PriceToVec
from use_strong_wifi import WifiStrongToVec
from use_wifi import WifiToVec
from use_wifi_kstrong import WifiKStrongToVec


class ModelTest(ModelBase):
    def __init__(self, save_model, use_multiprocess, save_result_proba):
        super().__init__(save_model=save_model, use_multiprocess=use_multiprocess, save_result_proba=save_result_proba)

    def _get_classifiers(self):
        """
        :return: dict. {name:classifier}
        """
        return {
            # 'light gbm': LGBMClassifier(n_jobs=self.n_jobs,
            #                             n_estimators=500,
            #                             learning_rate=0.05,
            #                             num_leaves=127,
            #                             max_depth=8,
            #                             ),
            'random forest': RandomForestClassifier(n_jobs=self.n_jobs,
                                                    n_estimators=400,
                                                    bootstrap=False,
                                                    min_samples_split=4,
                                                    min_samples_leaf=1,
                                                    random_state=self._random_state,
                                                    class_weight='balanced'),
            # 'binary random forest': OneVsRestClassifier(RandomForestClassifier(n_estimators=400,
            #                                                                    bootstrap=False,
            #                                                                    random_state=self._random_state,
            #                                                                    class_weight='balanced'),
            #                                             n_jobs=self.n_jobs),
            # 'xgb': XGBClassifier(colsample_bytree=0.7,
            #                      learning_rate=0.025,
            #                      max_depth=6,
            #                      min_child_weight=1,
            #                      missing=-999,
            #                      n_jobs=self.n_jobs,
            #                      n_estimators=500,
            #                      objective='binary:logistic',
            #                      random_state=1024,
            #                      _silent=1,
            #                      subsample=0.6),
            #
            # 'binary xgb': OneVsRestClassifier(XGBClassifier(colsample_bytree=0.7,
            #                                                 learning_rate=0.025,
            #                                                 max_depth=6,
            #                                                 min_child_weight=1,
            #                                                 missing=-999,
            #                                                 # n_jobs=os.cpu_count() // 3 * 2,
            #                                                 n_estimators=500,
            #                                                 objective='binary:logistic',
            #                                                 random_state=1024,
            #                                                 _silent=1,
            #                                                 subsample=0.6
            #                                                 )
            #                                   , n_jobs=self.n_jobs)
        }


def train_test():
    task = ModelTest(save_model=False, use_multiprocess=False, save_result_proba=True)
    vecs = [LocationToVec2(), WifiToVec(), WifiStrongToVec(), WifiKStrongToVec(), PriceToVec(),
            CategoryToVec2(),
            # UserToVec()
            ]
    print(vecs)
    task.train_test(vecs)
    task.train_and_on_test_data(vecs)


if __name__ == '__main__':
    train_test()
